<template>
  <player-buttons>
    <prev-button @repeatTrack="repeatTrack"></prev-button>
    <play-pause-button @click="playPauseTrack"></play-pause-button>
    <next-button @repeatTrack="repeatTrack"></next-button>
  </player-buttons>
</template>

<script>
import { defineComponent } from "vue";
import PrevButton from "@/components/player/buttons/PrevButton.vue";
import PlayPauseButton from "@/components/player/buttons/PlayPauseButton.vue";
import NextButton from "@/components/player/buttons/NextButton.vue";
import { mapMutations } from "vuex";

export default defineComponent({
  components: {
    PrevButton,
    PlayPauseButton,
    NextButton,
  },
  methods: {
    ...mapMutations({
      playPauseTrack: "player/playPauseTrack",
    }),
    repeatTrack() {
      this.$emit("repeatTrack");
    },
  },
});
</script>

<style></style>
