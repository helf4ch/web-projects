<template>
  <player-app></player-app>
  <explorer-app></explorer-app>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import PlayerApp from "@/components/player/PlayerApp.vue";
import ExplorerApp from "@/components/explorer/ExplorerApp.vue";
import { getFiles } from "@/hooks/getFiles";
import { getTracks } from "@/hooks/getTracks";
import { mapMutations } from "vuex";

export default defineComponent({
  components: {
    PlayerApp,
    ExplorerApp,
  },
  setup() {
    const { path, files } = getFiles();
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
      setAppPath: "explorer/setAppPath",
      setFilesArray: "explorer/setFilesArray",
    }),
  },
  created() {
    this.setTrackList(this.trackList);
    this.setAppPath(this.path);
    this.setFilesArray(this.files);
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
