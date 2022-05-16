<template>
  <player-app></player-app>
  <explorer-app @changeTrackList="changeTrackList"></explorer-app>
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
    const path = ref(app.getPath("music"));

    const { files } = getFiles(path);
    const { trackList } = getTracks(files);

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
    }),
    changeTrackList() {
      this.setPathToTrackList(this.path);
      this.setTrackList(this.trackList);
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
    files() {
      this.setFilesArray(this.files);
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
