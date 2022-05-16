<template>
  <audio ref="audio" style="display: none"></audio>
  <div ref="player" class="player">
    <equaliser-sliders
      :equaliserGainValues="equaliserGainValues"
    ></equaliser-sliders>
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
import EqualiserSliders from "@/components/player/EqualiserSliders.vue";
import ExplorerElementList from "@/components/explorer/ExplorerElementList.vue";
import ExplorerHeader from "@/components/explorer/ExplorerHeader.vue";
import { getFiles } from "@/hooks/getFiles";
import { getTracks } from "@/hooks/getTracks";
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
    EqualiserSliders,
  },
  setup() {
    let path = ref(app.getPath("music"));

    let { files } = getFiles(path);
    let { trackList } = getTracks(files);

    return {
      path,
      files,
      trackList,
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
    }),
    ...mapActions({
      onEnd: "player/onEnd",
    }),
    changeTrackList() {
      this.reloadPlayer();
      this.setPathToTrackList(this.path);
      this.setTrackList(this.trackList);
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
      this.$refs.audio.play();
    },
    pauseTrack() {
      this.$refs.audio.pause();
    },
    repeatTrack() {
      this.pauseTrack();
      this.loadTrack();
      this.playTrack();
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
          this.repeatTrack();
        }
        if (this.repeatType.repeatFolder && this.trackList.length === 1) {
          this.repeatTrack();
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
    audioVisuallizerAndEqualiser() {
      const canvasWidth = this.$refs.canvas.width;
      const canvasHeight = this.$refs.canvas.height;

      const audioContext = new AudioContext();
      const canvasContext = this.$refs.canvas.getContext("2d");

      const audioSource = audioContext.createMediaElementSource(
        this.$refs.audio
      );
      const analyser = audioContext.createAnalyser();

      function createFilter(frequency) {
        const filter = audioContext.createBiquadFilter();

        filter.type = "peaking";
        filter.frequency.value = frequency;
        filter.Q.value = 1;
        filter.gain.value = 0;

        return filter;
      }

      function createFilters() {
        const frequencies = [
          60, 170, 310, 600, 1000, 3000, 6000, 12000, 14000, 16000,
        ];
        const filters = frequencies.map(createFilter);

        filters.reduce(function (prev, curr) {
          prev.connect(curr);
          return curr;
        });

        return filters;
      }

      const filters = createFilters();

      audioSource.connect(filters[0]);
      audioSource.connect(analyser);
      filters[filters.length - 1].connect(audioContext.destination);
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
      currentPath: (state) => state.explorer.currentPath,
      isPlaying: (state) => state.player.isPlaying,
      trackList: (state) => state.player.trackList,
      trackIndex: (state) => state.player.trackIndex,
      repeatType: (state) => state.player.repeatType,
      pathToTrackList: (state) => state.player.pathToTrackList,
      isExplorerActive: (state) => state.explorer.isExplorerActive,
    }),
  },
  created() {
    this.setPathToTrackList(this.path);
    this.setTrackList(this.trackList);
    this.setAppPath(this.path);
    this.setFilesArray(this.files);
  },
  mounted() {
    this.loadTrack();
    this.initAudio();
    this.canvasInitialize();
    this.audioVisuallizerAndEqualiser();
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

.explorer-header {
  margin: 10px 0;
  text-align: center;
}
</style>
