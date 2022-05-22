<template>
  <div ref="player" class="player">
    <info-panel></info-panel>
    <equaliser-panel
      :equaliserGainValues="equaliserGainValues"
      @changeGainValueById="changeGainValueById"
    ></equaliser-panel>
    <detail-panel></detail-panel>
    <player-controll-buttons
      @repeatTrack="repeatTrack"
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
  <div v-if="isExplorerActive" class="explorer">
    <explorer-header @reloadExplorer="reloadExplorer"></explorer-header>
    <explorer-element-list
      @changeTrackList="changeTrackList"
    ></explorer-element-list>
  </div>
</template>

<script>
import { ref, defineComponent } from "vue";
import PlayerControllButtons from "@/components/player/PlayerControllButtons.vue";
import DetailPanel from "@/components/player/DetailPanel.vue";
import SlidersPanel from "@/components/player/SlidersPanel.vue";
import ButtonsPanel from "@/components/player/ButtonsPanel.vue";
import EqualiserPanel from "@/components/player/EqualiserPanel.vue";
import InfoPanel from "@/components/player/InfoPanel.vue";
import ExplorerElementList from "@/components/explorer/ExplorerElementList.vue";
import ExplorerHeader from "@/components/explorer/ExplorerHeader.vue";
import { getFiles } from "@/hooks/getFiles";
import { getTracks } from "@/hooks/getTracks";
import { initAudio } from "@/hooks/initAudio";
import { mapMutations, mapState, mapActions } from "vuex";
import { app } from "@electron/remote";

export default defineComponent({
  components: {
    PlayerControllButtons,
    DetailPanel,
    SlidersPanel,
    ButtonsPanel,
    ExplorerElementList,
    ExplorerHeader,
    EqualiserPanel,
    InfoPanel,
  },
  setup() {
    let path = ref(app.getPath("music"));

    let { files } = getFiles(path);
    let { tracks } = getTracks(files);

    const { audioElement, analyser, filters, visualiserDataArray } =
      initAudio();

    return {
      path,
      files,
      tracks,
      audioElement,
      analyser,
      filters,
      visualiserDataArray,
    };
  },
  data() {
    return {
      currentTime: 0,
      duration: 0,
      volumeValue: 50,
      equaliserGainValues: [
        { id: 0, gain: 0 },
        { id: 1, gain: 0 },
        { id: 2, gain: 0 },
        { id: 3, gain: 0 },
        { id: 4, gain: 0 },
        { id: 5, gain: 0 },
        { id: 6, gain: 0 },
        { id: 7, gain: 0 },
        { id: 8, gain: 0 },
        { id: 9, gain: 0 },
      ],
    };
  },
  methods: {
    ...mapMutations({
      setTrackList: "player/setTrackList",
      setPathToTrackList: "player/setPathToTrackList",
      setAppPath: "explorer/setAppPath",
      setFilesArray: "explorer/setFilesArray",
      reloadPlayer: "player/reloadPlayer",
      shuffleTrackList: "player/shuffleTrackList",
      setTrackIndex: "player/setTrackIndex",
      unshuffleTrackList: "player/unshuffleTrackList",
    }),
    ...mapActions({
      onEnd: "player/onEnd",
    }),
    changeTrackList() {
      this.reloadPlayer();
      this.setPathToTrackList(this.path);
      this.setTrackList(this.tracks);
      this.onTrackChange();
    },
    reloadExplorer() {
      this.path = "";
      this.path = app.getPath("music");
      this.changeTrackList();
      this.onTrackChange();
    },
    playPauseTrack() {
      if (this.isPlaying) {
        this.playTrack();
      } else {
        this.pauseTrack();
      }
    },
    playTrack() {
      if (this.audioElement.src != "") {
        this.audioElement.play();
      }
    },
    pauseTrack() {
      this.audioElement.pause();
    },
    repeatTrack() {
      this.pauseTrack();
      this.loadTrack();
      this.playTrack();
    },
    loadTrack() {
      if (this.trackList[this.trackIndex].path != "") {
        this.audioElement.src =
          "file://" + this.trackList[this.trackIndex].path;
      }
      this.audioElement.load();
    },
    onTrackChange() {
      this.pauseTrack();
      this.loadTrack();
      this.playPauseTrack();
    },
    updateCurrentTime(newValue) {
      this.currentTime = this.duration * (newValue / 100);
      this.audioElement.currentTime = this.currentTime;
    },
    updateVolumeValue(newValue) {
      this.volumeValue = newValue;
      this.audioElement.volume = this.volumeValue / 100;
    },
    changeGainValueById(gainValueId, newValue) {
      this.equaliserGainValues[gainValueId].gain = Number(newValue);
      if (this.isEqualiserTurnOn) {
        this.filters[gainValueId].gain.value = Number(newValue);
      }
    },
    setupCanvas() {
      this.$refs.canvas.width = this.$refs.player.clientWidth;
      this.$refs.canvas.height = this.$refs.player.clientHeight + 1;
    },
    setupAudio() {
      const audio = this.audioElement;
      audio.volume = this.volumeValue / 100;

      audio.ontimeupdate = () => {
        this.currentTime = audio.currentTime;
        this.setupCanvas();
      };

      audio.oncanplay = () => {
        this.duration = audio.duration;
      };

      audio.onended = () => {
        this.onEnd();

        if (this.repeatType.repeatTrack) {
          this.repeatTrack();
        }
        if (this.repeatType.repeatFolder && this.trackList.length === 1) {
          this.repeatTrack();
        }
        if (
          this.repeatType.repeatOff &&
          this.shuffleList.indexOf(this.trackIndex) == this.trackList.length - 1
        ) {
          this.pauseTrack();
          this.loadTrack();
        }
      };
    },
    animateVisualiser() {
      const canvasContext = this.$refs.canvas.getContext("2d");

      const bufferLength = this.analyser.frequencyBinCount;
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

      const canvasWidth = this.$refs.canvas.width;
      const canvasHeight = this.$refs.canvas.height;

      // const barOffset = canvasWidth / bufferLength - 10;
      const barOffset = 0;
      const barWidth = canvasWidth / bufferLength - barOffset;
      let x = canvasWidth / 2 + barOffset / 2;

      canvasContext.clearRect(0, 0, canvasWidth, canvasHeight);
      this.analyser.getByteFrequencyData(this.visualiserDataArray);

      for (let i = 0; i < bufferLength; i += 2) {
        let barHeight = (canvasHeight / 2 / 255) * this.visualiserDataArray[i];

        canvasContext.fillStyle = collorArray[(i / 2) % 8];
        canvasContext.fillRect(
          x,
          canvasHeight - barHeight,
          barWidth,
          barHeight
        );
        x += barWidth + barOffset;
      }

      x = canvasWidth / 2 - barWidth - barOffset / 2;

      for (let i = 1; i < bufferLength; i += 2) {
        let barHeight = (canvasHeight / 2 / 255) * this.visualiserDataArray[i];

        canvasContext.fillStyle = collorArray[Math.floor(i / 2) % 8];
        canvasContext.fillRect(
          x,
          canvasHeight - barHeight,
          barWidth,
          barHeight
        );
        x -= barWidth + barOffset;
      }

      requestAnimationFrame(this.animateVisualiser);
    },
  },
  computed: {
    ...mapState({
      currentPath: (state) => state.explorer.currentPath,
      isPlaying: (state) => state.player.isPlaying,
      trackIndex: (state) => state.player.trackIndex,
      repeatType: (state) => state.player.repeatType,
      pathToTrackList: (state) => state.player.pathToTrackList,
      isExplorerActive: (state) => state.explorer.isExplorerActive,
      isEqualiserTurnOn: (state) => state.player.isEqualiserTurnOn,
      isShuffleTurnOn: (state) => state.player.isShuffleTurnOn,
      trackList: (state) => state.player.trackList,
      shuffleList: (state) => state.player.shuffleList,
    }),
  },
  created() {
    this.setPathToTrackList(this.path);
    this.setTrackList(this.tracks);
    this.setAppPath(this.path);
    this.setFilesArray(this.files);
  },
  mounted() {
    this.loadTrack();
    this.setupAudio();
    this.setupCanvas();
    this.animateVisualiser();
  },
  watch: {
    currentPath() {
      this.path = this.currentPath;
    },
    files: {
      handler(newValue) {
        this.setFilesArray(newValue);
      },
      deep: true,
    },
    isPlaying() {
      this.playPauseTrack();
    },
    trackIndex() {
      this.onTrackChange();
    },
    isEqualiserTurnOn() {
      if (this.isEqualiserTurnOn) {
        for (let i = 0; i < 10; ++i) {
          this.filters[i].gain.value = this.equaliserGainValues[i].gain;
        }
      } else {
        for (let i = 0; i < 10; ++i) {
          this.filters[i].gain.value = 0;
        }
      }
    },
    isShuffleTurnOn() {
      if (this.isShuffleTurnOn) {
        this.shuffleTrackList();
      } else {
        this.unshuffleTrackList();
      }
    },
  },
});
</script>

<style>
body {
  background-color: #282828;
  color: #ebdbb2;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Roboto", sans-serif;
}

body::-webkit-scrollbar {
  width: 10px;
}

body::-webkit-scrollbar-track {
  background-color: #282828;
}

body::-webkit-scrollbar-thumb {
  background-color: #665c54;
  border-radius: 10px;
}

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

.explorer {
  border-top: 2px solid #665c54;
  margin: 30px 20px;
  padding: 0 25px;
  font-size: 1.1rem;
}
</style>
