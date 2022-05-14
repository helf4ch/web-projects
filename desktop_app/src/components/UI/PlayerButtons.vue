<template>
  <div class="player-btns">
    <slot></slot>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "player-buttons",
});
</script>

<style scoped>
.player-btns {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 5px 0px;
}
</style>
