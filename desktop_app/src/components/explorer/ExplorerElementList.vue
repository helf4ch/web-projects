<template>
  <div v-for="file in files" :key="file.name" class="explorer-element">
    <div class="explorer-element-content">
      <folder-icon v-if="file.isDirectory"></folder-icon>
      <music-file-icon v-else></music-file-icon>
      {{ file.name }}
      <div v-if="isThisFilePlaying(file)" class="align-self: flex-end;">
        playing
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { mapState } from "vuex";

import FolderIcon from "@/components/UI/icons/FolderIcon.vue";
import MusicFileIcon from "@/components/UI/icons/MusicFileIcon.vue";

export default defineComponent({
  components: {
    FolderIcon,
    MusicFileIcon,
  },
  methods: {
    isThisFilePlaying(file) {
      if (!this.isPlaying) {
        return false;
      }
      if (this.trackList[this.trackIndex].path === file.path) {
        return true;
      }
      return false;
    },
  },
  computed: {
    ...mapState({
      files: (state) => state.explorer.files,
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
}

.explorer-element-content:hover {
  opacity: 1;
}
</style>
