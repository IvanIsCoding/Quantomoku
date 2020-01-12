<template>
  <div class="main">
    <div v-for="line in board" :key="'line' + line[0].id" class="boardRow">
      <div v-for="cell in line" :key="cell.id" class="boardCell">
        <Cell
          @cellClicked="cellClicked"
          :id="cell.id"
          :selected="cell.id == selectedCells[0] || cell.id == selectedCells[1]"
          :value="cell.value"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Cell from "./Cell.vue";

export default {
  name: "BoardRenderer",
  components: {
    Cell
  },
  props: {
    selectedCells: Array,
    board: Array
  },
  methods: {
    cellClicked(id) {
      this.$emit("cellClicked", id);
    }
  }
};
</script>

<style>
.main {
  width: 760px;
  display: block;
  margin: auto;
  padding: 20px;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  background-image: url("../assets/board.png");
}

.boardRow {
  display: table-cell;
  justify-content: center;
}
</style>