
<template>
  <div class="hello">
    <button @click="devina">call devina function</button>
  </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js"></script>
<script>
//const socket = io("http://localhost:8000");
import io from "socket.io-client"
export default {
  name: "HelloWorld",
  props: {
    msg: String
  },
  methods: {
    devina: function() {
      const socket = io("http://localhost:8000");
      alert("devina function called");
      socket.emit("message", "HELLO WORLD");
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