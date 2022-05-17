<template>
  <player-button>
    <prev-button-icon @click="prevTrackHandler"></prev-button-icon>
  </player-button>
</template>

<script>
import { defineComponent } from "vue";
import PrevButtonIcon from "@/components/UI/icons/PrevButtonIcon.vue";
import { mapMutations, mapState } from "vuex";

export default defineComponent({
  components: {
    PrevButtonIcon,
  },
  methods: {
    ...mapMutations({
      prevTrack: "player/prevTrack",
    }),
    prevTrackHandler() {
      if (this.trackList.length === 1) {
        this.$emit("repeatTrack");
      } else {
        this.prevTrack();
      }
    },
  },
  computed: {
    ...mapState({
      trackList: (state) => state.player.trackList,
    }),
  },
});
</script>

<style></style>
