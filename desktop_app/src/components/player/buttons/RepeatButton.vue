<template>
  <player-button @click="this.switchRepeat">
    <arrow-repeat-icon
      class="active"
      v-if="$store.state.player.repeatType.repeatTrack"
    ></arrow-repeat-icon>
    <arrow-repeat-icon
      v-else-if="$store.state.player.repeatType.repeatFolder"
    ></arrow-repeat-icon>
    <arrow-repeat-icon v-else class="not-active"></arrow-repeat-icon>
  </player-button>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ArrowRepeatIcon from "@/components/UI/icons/ArrowRepeatIcon.vue";
import { mapMutations } from "vuex";

export default defineComponent({
  components: {
    ArrowRepeatIcon,
  },
  methods: {
    ...mapMutations({
      switchRepeat: "player/switchRepeat",
    }),
  },
});
</script>

<style scoped>
.active {
  color: #fabd2f;
}

.not-active {
  color: #665c54;
}
</style>
