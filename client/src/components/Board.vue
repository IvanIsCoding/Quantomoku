<template>
  <div class="main">
    <div v-for="line in cells" :key="'line' + line[0]" class="boardRow">
      <div v-for="cell in line" :key="cell.id" class="boardCell">
        <Cell :id="cell.id" @cellClicked="cellClicked" />
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
  methods: {
    make2dArray(d1, d2) {
      var count = 0;
      var arr = [];
      for (let i = 0; i < d2; i++) {
        var innerArray = [];
        for (let j = 0; j < d1; j++) {
          var myId = count++;
          innerArray.push({ id: myId });
        }
        arr.push(innerArray);
      }
      return arr;
    },
    cellClicked(id) {
      this.$emit("cellClicked", id);
    }
  },
  data() {
    return {
      cells: this.make2dArray(19, 19)
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