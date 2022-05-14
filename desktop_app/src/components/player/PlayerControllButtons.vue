<template>
  <player-buttons>
    <prev-button></prev-button>
    <play-pause-button
      :isPlaying="isPlaying"
      @click="PlayPauseTrack"
    ></play-pause-button>
    <next-button></next-button>
  </player-buttons>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PrevButton from "@/components/player/buttons/PrevButton.vue";
import PlayPauseButton from "@/components/player/buttons/PlayPauseButton.vue";
import NextButton from "@/components/player/buttons/NextButton.vue";
import { mapState } from "vuex";

export default defineComponent({
  components: {
    PrevButton,
    PlayPauseButton,
    NextButton,
  },
  methods: {
    PlayPauseTrack() {
      if (this.isPlaying) {
        this.$emit("pauseTrack");
      } else {
        this.$emit("playTrack");
      }
    },
  },
  computed: {
    ...mapState({
      isPlaying: (state: any) => state.player.isPlaying,
    }),
  },
});
</script>

<style></style>
