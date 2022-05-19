<template>
  <div class="info">
    <div class="track-number" v-if="trackList">
      {{ trackIndex + 1 }} OF {{ trackList.length }}
    </div>
    <div class="track-path" v-if="pathToTrackList">
      {{ pathToTrackList }}
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { mapState } from "vuex";

export default defineComponent({
  computed: {
    ...mapState({
      trackIndex: (state) => state.player.trackIndex,
      trackList: (state) => state.player.trackList,
      pathToTrackList: (state) => state.player.pathToTrackList,
    }),
  },
});
</script>

<style scoped>
.info {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  padding: 5px 0px;
}

.track-path {
  font-size: 0.8rem;
  text-align: center;
  padding: 3px 0;
}

.track-number {
  font-size: 1rem;
  text-align: center;
  padding: 3px 0;
}
</style>
