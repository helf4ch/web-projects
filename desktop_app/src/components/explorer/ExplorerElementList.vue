<template>
  <div v-for="file in files" :key="file.name" class="explorer-element">
    <div class="explorer-element-content" @click="fileHandler(file)">
      <div>
        <folder-icon v-if="file.isDirectory"></folder-icon>
        <music-file-choosen-icon
          v-else-if="isThisFileChoosen(file)"
        ></music-file-choosen-icon>
        <music-file-icon v-else></music-file-icon>
        {{ file.name }}
      </div>
      <div class="explorer-file-status">
        <div v-if="isThisFilePlaying(file)">playing</div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { mapState, mapMutations } from "vuex";

import FolderIcon from "@/components/UI/icons/FolderIcon.vue";
import MusicFileIcon from "@/components/UI/icons/MusicFileIcon.vue";
import MusicFileChoosenIcon from "@/components/UI/icons/MusicFileChoosenIcon.vue";

export default defineComponent({
  components: {
    FolderIcon,
    MusicFileIcon,
    MusicFileChoosenIcon,
  },
  emits: ["changeTrackList"],
  methods: {
    ...mapMutations({
      playPauseTrack: "player/playPauseTrack",
      setTrackIndex: "player/setTrackIndex",
      setAppPath: "explorer/setAppPath",
    }),
    isThisFileChoosen(file) {
      if (this.trackList[this.trackIndex].path === file.path) {
        return true;
      }
      return false;
    },
    isThisFilePlaying(file) {
      if (!this.isPlaying) {
        return false;
      }
      return this.isThisFileChoosen(file);
    },
    fileHandler(file) {
      if (file.isDirectory) {
        this.setAppPath(file.path);
      } else {
        if (this.isThisFileChoosen(file)) {
          this.playPauseTrack();
        } else {
          if (this.currentPath !== this.pathToTrackList) {
            this.$emit("changeTrackList");
          }
          this.setTrackIndex(
            this.trackList.findIndex((el) => el.path === file.path)
          );
        }
      }
    },
  },
  computed: {
    ...mapState({
      files: (state) => state.explorer.files,
      currentPath: (state) => state.explorer.currentPath,
      pathToTrackList: (state) => state.player.pathToTrackList,
      isPlaying: (state) => state.player.isPlaying,
      trackList: (state) => state.player.trackList,
      trackIndex: (state) => state.player.trackIndex,
    }),
  },
});
</script>

<style scoped>
.explorer-element {
  margin: 10px 0;
  padding: 10px 10px 0;
  border-top: 2px solid #665c54;
}

.explorer-element-content {
  opacity: 0.8;
  transition: opacity 0.2s;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.explorer-element-content:hover {
  opacity: 1;
}

.explorer-file-status {
  /* display: flex; */
}
</style>
