<template>
  <audio ref="audio" style="display: none"></audio>
  <div ref="player" class="player">
    <detail-panel></detail-panel>
    <player-controll-buttons></player-controll-buttons>
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
import { mapState, mapActions } from "vuex";

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
    ...mapActions({
      onEnd: "player/onEnd",
    }),
    playPauseTrack() {
      if (this.isPlaying) {
        this.playTrack();
      } else {
        this.pauseTrack();
      }
    },
    playTrack() {
      this.$refs.audio.play();
    },
    pauseTrack() {
      this.$refs.audio.pause();
    },
    loadTrack() {
      this.$refs.audio.src = "file://" + this.trackList[this.trackIndex].path;
      this.$refs.audio.load();
    },
    onTrackChange() {
      this.pauseTrack();
      this.loadTrack();
      this.playPauseTrack();
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

      const collorArray = [
        "#cc241d",
        "#d65d0e",
        "#d79921",
        "#98971a",
        "#689d6a",
        "#458588",
        "#b16286",
        "#928374",
      ];

      function animate() {
        let x = canvasWidth / 2;

        canvasContext.clearRect(0, 0, canvasWidth, canvasHeight);
        analyser.getByteFrequencyData(dataArray);

        for (let i = 0; i < bufferLength; i += 2) {
          let barHeight = (canvasHeight / 2 / 255) * dataArray[i];

          canvasContext.fillStyle = collorArray[(i / 2) % 8];
          canvasContext.fillRect(
            x,
            canvasHeight - barHeight,
            barWidth,
            barHeight
          );
          x += barWidth;
        }

        x = canvasWidth / 2 - barWidth;

        for (let i = 1; i < bufferLength; i += 2) {
          let barHeight = (canvasHeight / 2 / 255) * dataArray[i];

          canvasContext.fillStyle = collorArray[Math.floor(i / 2) % 8];
          canvasContext.fillRect(
            x,
            canvasHeight - barHeight,
            barWidth,
            barHeight
          );
          x -= barWidth;
        }

        requestAnimationFrame(animate);
      }

      animate();
    },
  },
  computed: {
    ...mapState({
      isPlaying: (state) => state.player.isPlaying,
      trackList: (state) => state.player.trackList,
      trackIndex: (state) => state.player.trackIndex,
      repeatType: (state) => state.player.repeatType,
      pathToTrackList: (state) => state.player.pathToTrackList,
    }),
  },
  watch: {
    trackIndex() {
      this.onTrackChange();
    },
    isPlaying() {
      this.playPauseTrack();
    },
    pathToTrackList() {
      this.onTrackChange();
    },
  },
  mounted() {
    this.loadTrack();
    this.initAudio();
    this.canvasInitialize();
    this.audioVisuallizer();
  },
});
</script>

<style scoped>
.player {
  border-radius: 14px;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  margin: 20px;
  padding: 25px;
  border: 5px solid #665c54;
}

.canvas {
  position: absolute;
  z-index: -1;
  border-radius: 5px;
  opacity: 0.8;
}
</style>
