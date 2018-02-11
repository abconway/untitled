<template>
<div>
    <div class="button" v-on:click="toggle()" v-show="active">
        <img class="edit" src="../assets/pencil.svg">
    </div>
    <div class="button" v-on:click="toggle(); discard()" v-show="!active">
        <img class="discard" src="../assets/x.svg">
    </div>
    <div class="button" v-on:click="toggle(); accept()" v-show="!active">
        <img class="accept" src="../assets/checkmark.svg">
    </div>
    <div class="text" v-show="active">
        {{ title }}
    </div>
    <div class="container" v-show="!active">
        <input class="input" v-model="temporary_title">
        <div class="slug">slug: {{ slug }}</div>
    </div>
</div>
</template>

<script>
export default {
  name: 'Title',
  computed: {
    slug() {
      return this.temporary_title.toString().toLowerCase()
        .replace(/\s+/g, '-')
        .replace(/&/g, '-and-')
        .replace(/[^\w-]+/g, '')
        .replace(/-+/g, '-')
        .replace(/^-+/, '')
        .replace(/-+$/, '');
    },
  },
  data() {
    return {
      title: 'I knew you were trouble when you walked in.',
      temporary_title: 'I knew you were trouble when you walked in.',
      active: true,
    };
  },
  methods: {
    accept() {
      this.title = this.temporary_title;
    },
    discard() {
      this.temporary_title = this.title;
    },
    toggle() {
      this.active = !this.active;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
    margin: 0;
    padding: 0;
}
img {
    height: 25px;
    width: 25px;
}
.accept {
    background-color: green;
}
.button {
    height: 25px;
    right: 25px;
    bottom: 6px;
    position: relative;
    width: 25px;
}
.container{
    background-color: white;
    padding: 0.5em;
    width: 100%;
}
.discard {
    background-color: red;
}
.edit {
    background-color: yellow;
}
.input {
    font-size: 2em;
}
.slug {
    font-size: 10px;
}
.text {
    background-color: white;
    display: inline;
    font-size: 2em;
    padding: 0.2em;
}
</style>
