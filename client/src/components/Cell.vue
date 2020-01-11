<template>
  <span>
    <img src="../assets/cell.png" width="20px" height="20px" />
  </span>
</template>

<script>
export default {
  name: "Cell",
  props: {
    msg: String
  }
};
</script>

<style scoped>
img {
  text-align: center;
  display: block;
}
</style>