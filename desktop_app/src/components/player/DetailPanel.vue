<template>
  <div class="details">
    <div class="track-title" v-if="this.trackList[this.trackIndex].title">
      {{ this.trackList[this.trackIndex].title }}
    </div>
    <div class="track-title" v-else>Unknown</div>
    <div class="track-artist" v-if="this.trackList[this.trackIndex].artist">
      {{ this.trackList[this.trackIndex].artist }}
    </div>
    <div class="track-artist" v-else>Unknown</div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapState } from "vuex";

export default defineComponent({
  computed: {
    ...mapState({
      trackList: (state: any) => state.player.trackList,
      trackIndex: (state: any) => state.player.trackIndex,
    }),
  },
});
</script>

<style scoped>
.details {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  padding: 5px 0px;
}

.track-title {
  font-size: 3rem;
}

.track-artist {
  font-size: 1.5rem;
}
</style>
