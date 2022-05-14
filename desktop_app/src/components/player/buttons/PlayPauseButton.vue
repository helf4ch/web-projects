<template>
  <player-button>
    <play-button-icon v-if="!$store.state.player.isPlaying"></play-button-icon>
    <pause-button-icon v-else></pause-button-icon>
  </player-button>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import PlayButtonIcon from "@/components/UI/icons/PlayButtonIcon.vue";
import PauseButtonIcon from "@/components/UI/icons/PauseButtonIcon.vue";

export default defineComponent({
  components: {
    PlayButtonIcon,
    PauseButtonIcon,
  },
});
</script>

<style></style>
