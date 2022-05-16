<template>
  <player-button>
    <next-button-icon @click="nextTrackHandler"></next-button-icon>
  </player-button>
</template>

<script>
import { defineComponent } from "vue";
import NextButtonIcon from "@/components/UI/icons/NextButtonIcon.vue";
import { mapMutations, mapState } from "vuex";

export default defineComponent({
  components: {
    NextButtonIcon,
  },
  methods: {
    ...mapMutations({
      nextTrack: "player/nextTrack",
    }),
    nextTrackHandler() {
      if (this.trackList.length === 1) {
        this.$emit("repeatTrack");
      } else {
        this.nextTrack();
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
