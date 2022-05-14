<template>
  <audio ref="audio" style="display: none"></audio>
  <div ref="player" class="player">
    <detail-panel></detail-panel>
    <player-controll-buttons
      @playTrack="playTrack"
      @pauseTrack="pauseTrack"
    ></player-controll-buttons>
    <sliders-panel
      :currentTime="currentTime"
      :duration="duration"
      :volumeValue="volumeValue"
      @updateCurrentTime="updateCurrentTime"
      @updateVolumeValue="updateVolumeValue"
    ></sliders-panel>
    <buttons-panel></buttons-panel>
    <canvas ref="canvas" class="canvas"></canvas>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import PlayerControllButtons from "@/components/player/PlayerControllButtons.vue";
import DetailPanel from "@/components/player/DetailPanel.vue";
import SlidersPanel from "@/components/player/SlidersPanel.vue";
import ButtonsPanel from "@/components/player/ButtonsPanel.vue";
import { mapMutations, mapState, mapActions } from "vuex";

export default defineComponent({
  components: {
    PlayerControllButtons,
    DetailPanel,
    SlidersPanel,
    ButtonsPanel,
  },
  data() {
    return {
      currentTime: 0,
      duration: 0,
      volumeValue: 50,
    };
  },
  methods: {
    ...mapMutations({
      setIsPlaying: "player/setIsPlaying",
    }),
    ...mapActions({
      onEnd: "player/onEnd",
    }),
    canvasInitialize() {
      this.$refs.canvas.width = this.$refs.player.clientWidth;
      this.$refs.canvas.height = this.$refs.player.clientHeight;
    },
    audioVisuallizer() {
      const canvasWidth = this.$refs.canvas.width;
      const canvasHeight = this.$refs.canvas.height;
      const audioContext = new AudioContext();
      const canvasContext = this.$refs.canvas.getContext("2d");

      const audioSource = audioContext.createMediaElementSource(
        this.$refs.audio
      );
      const analyser = audioContext.createAnalyser();

      audioSource.connect(analyser);
      analyser.connect(audioContext.destination);

      analyser.fftSize = 32;

      const bufferLength = analyser.frequencyBinCount;
      const dataArray = new Uint8Array(bufferLength);

      const barWidth = canvasWidth / bufferLength;

      function animate() {
        let x = 0;

        console.log(canvasWidth);

        canvasContext.clearRect(0, 0, canvasWidth, canvasHeight);
        analyser.getByteFrequencyData(dataArray);

        for (let i = 0; i < bufferLength; ++i) {
          let barHeight = dataArray[i];
          canvasContext.fillStyle = "white";
          canvasContext.fillRect(
            x,
            canvasHeight - barHeight,
            barWidth,
            barHeight
          );
          x += barWidth;
        }

        requestAnimationFrame(animate);
      }

      animate();
    },
    playTrack() {
      this.$refs.audio.play();
      this.setIsPlaying(true);
      this.audioVisuallizer();
      // var playPromise = this.$refs.audio.play();

      // if (playPromise !== undefined) {
      //   playPromise
      //     .then((_) => {
      //       console.log(_);
      //     })
      //     .catch((error) => {
      //       console.log(error);
      //     });
      // }
    },
    pauseTrack() {
      this.$refs.audio.pause();
      this.setIsPlaying(false);
    },
    loadTrack() {
      this.$refs.audio.src = "file://" + this.trackList[this.trackIndex].path;
      this.$refs.audio.load();
    },
    updateCurrentTime(newValue) {
      this.currentTime = this.duration * (newValue / 100);
      this.$refs.audio.currentTime = this.currentTime;
    },
    updateVolumeValue(newValue) {
      this.volumeValue = newValue;
      this.$refs.audio.volume = this.volumeValue / 100;
    },
    initAudio() {
      const audio = this.$refs.audio;
      audio.volume = this.volumeValue / 100;

      audio.ontimeupdate = () => {
        this.currentTime = audio.currentTime;
      };

      audio.oncanplay = () => {
        this.duration = audio.duration;
      };

      audio.onended = () => {
        this.onEnd();

        if (this.repeatType.repeatTrack) {
          this.pauseTrack();
          this.loadTrack();
          this.playTrack();
        }
        if (
          this.repeatType.repeatOff &&
          this.trackIndex == this.trackList.length - 1
        ) {
          this.pauseTrack();
          this.loadTrack();
        }
      };
    },
  },
  computed: {
    ...mapState({
      isPlaying: (state) => state.player.isPlaying,
      trackList: (state) => state.player.trackList,
      trackIndex: (state) => state.player.trackIndex,
      repeatType: (state) => state.player.repeatType,
    }),
  },
  watch: {
    trackIndex() {
      this.pauseTrack();
      this.loadTrack();
      this.playTrack();
    },
  },
  mounted() {
    this.loadTrack();
    this.initAudio();
    this.canvasInitialize();
  },
});
</script>

<style scoped>
.player {
  /* background-color: #928374; */
  border-radius: 14px;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  margin: 20px;
  padding: 25px;
}

.canvas {
  position: absolute;
  z-index: -1;
  border-radius: 14px;
}
</style>
