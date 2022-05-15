<template>
  <player-buttons>
    <prev-button></prev-button>
    <play-pause-button @click="playPauseTrack"></play-pause-button>
    <next-button></next-button>
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
  },
});
</script>

<style></style>
