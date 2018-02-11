<template>
<div>
    <div class="button" v-on:click="toggle()" v-show="active">
        <img class="edit" src="../assets/pencil.svg">
    </div>
    <div class="button" v-on:click="toggle(); discard()" v-show="!active">
        <img class="discard" src="../assets/x.svg">
    </div>
    <div class="button" v-on:click="toggle(); accept()" v-show="!active&&!empty">
        <img class="accept" src="../assets/checkmark.svg">
    </div>
    <div class="button" v-show="!active&&empty">
        <img class="cant-accept" src="../assets/checkmark.svg">
    </div>
    <div class="text" v-show="active">
        {{ title }}
    </div>
    <div class="container" v-show="!active">
        <input class="input" v-model="temporaryTitle">
        <div class="slug" v-show="!empty">
            <span class="gray">slug:</span> {{ slug }}
        </div>
        <div class="slug" v-show="empty">
            <span class="gray">slug: <i>please enter a post title</i></span>
        </div>
    </div>
</div>
</template>

<script>
export default {
  name: 'Title',
  created() {
    this.axios.get('http://localhost:8000/api/titles/').then((response) => {
      this.currentTitleId = response.data[0].id;
      this.title = response.data[0].name;
      this.temporaryTitle = response.data[0].name;
    });
  },
  computed: {
    empty() {
      return this.slug.length === 0;
    },
    slug() {
      const calculatedSlug = this.temporaryTitle.toString().toLowerCase()
        .replace(/\s+/g, '-')
        .replace(/&/g, '-and-')
        .replace(/[^\w-]+/g, '')
        .replace(/-+/g, '-')
        .replace(/^-+/, '')
        .replace(/-+$/, '');
      if (this.slugCollision) {
        return `${calculatedSlug}-${this.slugRandomizer()}`;
      }
      return calculatedSlug;
    },
  },
  data() {
    return {
      active: true,
      currentTitleId: 0,
      slugCollision: false,
      title: 'I knew you were trouble when you walked in.',
      temporaryTitle: 'I knew you were trouble when you walked in.',
    };
  },
  methods: {
    accept() {
      this.title = this.temporaryTitle;
      this.axios.post('http://localhost:8000/api/titles/', {
        name: this.title,
        slug: this.slug,
      });
    },
    discard() {
      this.temporaryTitle = this.title;
    },
    slugRandomizer() {
      return Math.random().toString(36).substring(2, 7);
    },
    toggle() {
      this.active = !this.active;
    },
  },
  watch: {
    temporaryTitle() {
      this.axios.get(`http://localhost:8000/api/titles/?slug=${this.slug}`).then((response) => {
        if (response.data.length > 0) {
          console.log('It already exists');
          const foundTitleId = response.data[0].id;
          if (foundTitleId === this.currentTitleId) {
            console.log('But its the same as our current title');
            this.slugCollision = false;
          } else {
            this.slugCollision = true;
          }
        } else {
          this.slugCollision = false;
        }
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@font-face {
    font-family: 'copernicus-heavy';
    src: url('../fonts/copernicus_webfont/Copernicus-Heavy.eot?') format('eot'),
         url('../fonts/copernicus_webfont/Copernicus-Heavy.woff') format('woff'),
         url('../fonts/copernicus_webfont/Copernicus-Heavy.ttf') format('truetype');
}
div {
    margin: 0;
    padding: 0;
}
img {
    height: 25px;
    width: 25px;
}
.accept {
    background-color: limegreen;
}
.button {
    height: 25px;
    right: 25px;
    bottom: 6px;
    position: relative;
    width: 25px;
}
.cant-accept {
    background-color: darkslategray;
}
.container{
    background-color: white;
    padding: 0.5em;
    width: 100%;
}
.discard {
    background-color: orangered;
}
.edit {
    background-color: yellow;
}
.gray {
    color: darkgray;
}
.input {
    font-size: 2em;
    font-family: copernicus-heavy;
    font-size: 2em;
}
.slug {
    font-family: Futura;
    font-size: 10px;
}
.text {
    background-color: white;
    color: black;
    display: inline;
    font-family: copernicus-heavy;
    font-size: 2.5em;
    padding: 0.2em;
}
</style>
