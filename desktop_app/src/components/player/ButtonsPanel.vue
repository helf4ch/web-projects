<template>
  <player-buttons>
    <repeat-button></repeat-button>
  </player-buttons>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import RepeatButton from "@/components/player/buttons/RepeatButton.vue";

export default defineComponent({
  components: {
    RepeatButton,
  },
});
</script>

<style></style>
