<template>
  <player-button @click="this.switchRepeat">
    <arrow-clockwise-icon
      v-if="$store.state.player.repeatType.repeatTrack"
    ></arrow-clockwise-icon>
    <arrow-repeat-icon
      v-else-if="$store.state.player.repeatType.repeatFolder"
    ></arrow-repeat-icon>
    <arrow-next-icon v-else></arrow-next-icon>
  </player-button>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ArrowRepeatIcon from "@/components/UI/icons/ArrowRepeatIcon.vue";
import ArrowClockwiseIcon from "@/components/UI/icons/ArrowClockwiseIcon.vue";
import ArrowNextIcon from "@/components/UI/icons/ArrowNextIcon.vue";
import { mapMutations } from "vuex";

export default defineComponent({
  components: {
    ArrowRepeatIcon,
    ArrowClockwiseIcon,
    ArrowNextIcon,
  },
  methods: {
    ...mapMutations({
      switchRepeat: "player/switchRepeat",
    }),
  },
});
</script>

<style></style>
