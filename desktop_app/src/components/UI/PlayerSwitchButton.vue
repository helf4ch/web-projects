<template>
  <input type="checkbox" :checked="checked" class="toggle-button" />
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "player-switch-button",
  props: {
    checked: [Boolean],
  },
});
</script>

<style scoped>
.toggle-button {
  opacity: 0.7;
  -webkit-transition: 0.2s;
  transition: opacity 0.2s;
  position: relative;
  width: 70px;
  height: 35px;
  margin: 0;
  vertical-align: top;
  background: #665c54;
  border-radius: 30px;
  outline: none;
  cursor: pointer;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  transition: all 0.3s cubic-bezier(0.2, 0.85, 0.32, 1.2);
}

.toggle-button:hover {
  opacity: 1;
}

.toggle-button::after {
  content: "";
  position: absolute;
  left: 3px;
  top: 2px;
  width: 30px;
  height: 30px;
  background-color: #ebdbb2;
  border-radius: 50%;
  transform: translateX(0);
  transition: all 0.3s cubic-bezier(0.2, 0.85, 0.32, 1.2);
}

.toggle-button:checked::after {
  transform: translateX(calc(100% + 3px));
  background-color: #665c54;
}

.toggle-button:checked {
  background-color: #ebdbb2;
}
</style>
