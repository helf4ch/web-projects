<template>
  <div class="btn">
    <slot></slot>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "player-button",
});
</script>

<style scoped>
.btn {
  margin: 6px 20px 0px;
  color: #ebdbb2;
  opacity: 0.8;
  transition: opacity 0.2s;
  cursor: pointer;
}

.btn:hover {
  opacity: 1;
}
</style>
