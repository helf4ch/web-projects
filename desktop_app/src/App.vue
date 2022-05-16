<template>
  <player-app></player-app>
  <explorer-app
    @changeTrackList="changeTrackList"
    @reloadExplorer="reloadExplorer"
  ></explorer-app>
</template>

<script>
import { ref, defineComponent } from "vue";

import PlayerApp from "@/components/player/PlayerApp.vue";
import ExplorerApp from "@/components/explorer/ExplorerApp.vue";
import { getFiles } from "@/hooks/getFiles";
import { getTracks } from "@/hooks/getTracks";
import { mapMutations, mapState } from "vuex";
import { app } from "@electron/remote";

export default defineComponent({
  components: {
    PlayerApp,
    ExplorerApp,
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
  methods: {
    ...mapMutations({
      setTrackList: "player/setTrackList",
      setPathToTrackList: "player/setPathToTrackList",
      setAppPath: "explorer/setAppPath",
      setFilesArray: "explorer/setFilesArray",
      reloadPlayer: "player/reloadPlayer",
    }),
    changeTrackList() {
      this.setPathToTrackList(this.path);
      this.setTrackList(this.trackList);
    },
    reloadExplorer() {
      // this.path = "";
      // this.path = app.getPath("music");
      // this.setAppPath(this.path);
      // // this.files = getFiles(this.path);
      // // this.changeTrackList();
      // // this.$forceUpdate();
      // this.changeTrackList();
      // this.reloadPlayer();
    },
  },
  computed: {
    ...mapState({
      currentPath: (state) => state.explorer.currentPath,
    }),
  },
  created() {
    this.changeTrackList();
    this.setAppPath(this.path);
    this.setFilesArray(this.files);
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
</style>
