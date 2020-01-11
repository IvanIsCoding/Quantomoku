<template>
  <!-- <div class="hello">Our cool QuantumOku</div> -->
  <div>
    <li v-for="cell in cells">
      </Cell>
    </li>
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
  data() {
    return {
      cells: [0, 0, 0]
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
