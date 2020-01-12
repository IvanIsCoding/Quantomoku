<template>
  <div class="main">
    <div v-for="line in cells" :key="'line' + line[0]" class="boardRow">
      <div v-for="cell in line" :key="cell.id" class="boardCell">
        <Cell
          :id="cell.id"
          @cellClicked="cellClicked"
          :selected="cell.id == selectedCells[0] || cell.id == selectedCells[1]"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Cell from "./Cell.vue";

export default {
  name: "Board",
  components: {
    Cell
  },
  props: {
    selectedCells: Array
  },
  methods: {
    make2dArray(rows, columns) {
      var result = [];
      for (var i = 0; i < rows; i++) {
        var row = [];
        for (var j = 0; j < columns; j++) {
          row.push({ id: i + "" + j });
        }
        result.push(row);
      }
      print2dArray(result);
      return result;
    },
    print2dArray(matrix) {
      for(var i = 0; i < matrix.length; i++) {
        for(var j = 0; < )
      }
    },
    cellClicked(id) {
      this.$emit("cellClicked", id);
    }
  },
  data() {
    return {
      cells: this.make2dArray(5, 5)
    };
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