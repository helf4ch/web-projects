<template>
  <div class="details">
    <div class="track-title" v-if="trackList[trackIndex].title">
      {{ trackList[trackIndex].title }}
    </div>
    <div class="track-title" v-else>Unknown</div>
    <div class="track-artist" v-if="trackList[trackIndex].artist">
      {{ trackList[trackIndex].artist }}
    </div>
    <div class="track-artist" v-else>Unknown</div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { mapState } from "vuex";

export default defineComponent({
  computed: {
    ...mapState({
      trackList: (state) => state.player.trackList,
      trackIndex: (state) => state.player.trackIndex,
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
