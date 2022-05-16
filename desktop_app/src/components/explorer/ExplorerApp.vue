<template>
  <div class="explorer">
    <explorer-header @reloadExplorer="reloadExplorer"></explorer-header>
    <explorer-element-list
      @changeTrackList="changeTrackList"
    ></explorer-element-list>
  </div>
</template>

<script>
import { defineComponent } from "vue";

import ExplorerElementList from "@/components/explorer/ExplorerElementList.vue";
import ExplorerHeader from "@/components/explorer/ExplorerHeader.vue";

export default defineComponent({
  components: {
    ExplorerElementList,
    ExplorerHeader,
  },
  emits: ["changeTrackList", "reloadExplorer"],
  methods: {
    changeTrackList() {
      this.$emit("changeTrackList");
    },
    reloadExplorer() {
      this.$emit("reloadExplorer");
    },
  },
});
</script>

<style scoped>
.explorer {
  border-top: 2px solid #665c54;
  margin: 30px 20px;
  padding: 0 25px;
  font-size: 1.1rem;
}

.explorer-header {
  margin: 10px 0;
  text-align: center;
}
</style>
