<template>
  <player-buttons>
    <repeat-button></repeat-button>
    <show-explorer-button></show-explorer-button>
  </player-buttons>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import RepeatButton from "@/components/player/buttons/RepeatButton.vue";
import ShowExplorerButton from "@/components/player/buttons/ShowExplorerButton.vue";

export default defineComponent({
  components: {
    RepeatButton,
    ShowExplorerButton,
  },
});
</script>

<style></style>
