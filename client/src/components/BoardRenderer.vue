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
  border-color:rgb(117, 54, 2);
  border-style:solid;
  border-radius: 5px;
  border-width: 10px;
  width: auto;
  display: block;
  margin: auto;
  background-image: url("../assets/board.png");
}

.boardRow {
  display: table-cell;
  justify-content: center;
}
</style>