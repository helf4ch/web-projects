<template>
  <player-button @click="this.switchRepeat">
    <arrow-repeat-icon
      :class="{
        active: repeatType.repeatTrack,
        'not-active': repeatType.repeatOff,
      }"
    ></arrow-repeat-icon>
  </player-button>
</template>

<script>
import { defineComponent } from "vue";
import ArrowRepeatIcon from "@/components/UI/icons/ArrowRepeatIcon.vue";
import { mapMutations, mapState } from "vuex";

export default defineComponent({
  components: {
    ArrowRepeatIcon,
  },
  methods: {
    ...mapMutations({
      switchRepeat: "player/switchRepeat",
    }),
  },
  computed: {
    ...mapState({
      repeatType: (state) => state.player.repeatType,
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
