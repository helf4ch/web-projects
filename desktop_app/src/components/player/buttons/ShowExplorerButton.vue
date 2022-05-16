<template>
  <player-button @click="changeExplorerActive">
    <music-list-icon v-if="isExplorerActive" class="active"></music-list-icon>
    <music-list-icon v-else></music-list-icon>
  </player-button>
</template>

<script>
import { defineComponent } from "vue";
import MusicListIcon from "@/components/UI/icons/MusicListIcon.vue";
import { mapMutations, mapState } from "vuex";

export default defineComponent({
  components: {
    MusicListIcon,
  },
  methods: {
    ...mapMutations({
      changeExplorerActive: "explorer/changeExplorerActive",
    }),
  },
  computed: {
    ...mapState({
      isExplorerActive: (state) => state.explorer.isExplorerActive,
    }),
  },
});
</script>

<style scoped>
.active {
  color: #fabd2f;
}
</style>
