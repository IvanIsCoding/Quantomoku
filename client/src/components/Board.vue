<template>
  <!-- <div class="hello">Our cool QuantumOku</div> -->
  <div>
    <div v-for="line in cells" :key="line[0]">
      <span v-for="cell in line" :key="cell">
        <Cell />
      </span>
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