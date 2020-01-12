<template>
  <!-- <div class="hello">Our cool QuantumOku</div> -->
  <div class="main">
    <div v-for="line in cells" :key="line[0]" class="boardRow">
      <div v-for="cell in line" :key="cell" class="boardCell">
        <Cell />
      </div>
    </div>
  </div>
</template>

<script>
import Cell from "./Cell.vue";

export default {
  name: "Board",
  props: {
    msg: String
  },
  components: {
    Cell
  },
  methods: {
    make2dArray(d1, d2) {
      var count = 0;
      var arr = [];
      for (let i = 0; i < d2; i++) {
        var innerArray = [count++];
        for (let j = 0; j < d1; j++) {
          innerArray.push(count++);
        }
        arr.push(innerArray);
      }
      return arr;
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

.boardRow {
  display: flex;
}

</style>