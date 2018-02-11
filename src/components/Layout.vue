<template>
<div>
    <div class="width-100 background-image">
        <div class="fixed absolute left">&nbsp;</div>
        <div class="content top absolute">
            <div class="row top left absolute">
                <div class="column width-75"></div>
                <div class="column text-right width-25">
                    <img src="../assets/logo_and_hamburger.svg">
                </div>
            </div>
            <div class="row bottom absolute">
                <div class="column width-12_5"></div>
                <div class="column relative offset width-62_5">
                    <h1 class="width-85">
                        I knew you were trouble when you walked in.
                    </h1>
                </div>
                <div class="column width-25"></div>
            </div>
        </div>
        <div class="fixed absolute right">&nbsp;</div>
    </div>
    <div class="width-100">
        <div class="fixed left">&nbsp;</div>
        <div class="content">
            <div class="row">
                <div class="column width-12_5"></div>
                <div class="column width-25">
                    <div class="width-75"><hr></div>
                    <p>By: Bob Loblaw</p>
                    <div class="width-75"><hr></div>
                    <p>Aug, 6 2015</p>
                    <div class="width-75"><hr></div>
                    <span>#ENVIRONMENT</span><br>
                    <span>#SWIFT</span><br>
                    <span>#FUNGUS</span><br>
                </div>
                <div class="column width-50" style="vertical-align: top;">
                    <p>
                        NEW YORK, NY. Nunc eu ullamcorper orci. Quisque eget odio ac lectus
                        vestibulum faucibus eget in metus. In pellentesque faucibus vestibulum.
                        Nulla at nulla justo, eget luctus tortor. Nulla facilisi. Duis aliquet
                        egestas purus in blandit. Curabitur vulputate, ligula lacinia scelerisque
                        tempor, lacus lacus ornare ante, ac egestas est urna sit amet arcu. Class
                        aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos
                        himenaeos. Sed molestie augue sit amet leo consequat posuere.
                    </p>
                    <p>
                        Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere
                        cubilia Curae; Proin vel ante a orci tempus eleifend ut et magna. Lorem
                        ipsum dolor sit amet, consectetur adipiscing elit. Vivamus luctus urna sed
                        urna ultricies ac tempor dui sagittis. In condimentum facilisis porta. Sed
                        nec diam eu diam mattis viverra. Nulla fringilla, orci ac euismod semper,
                        magna diam porttitor mauris, quis sollicitudin sapien justo in libero.
                        Vestibulum mollis mauris enim.
                    </p>
                </div>
                <div class="column width-12_5"></div>
            </div>
            <div class="row" style="margin-bottom: 1em;">
                <div class="column width-25"></div>
                <div class="column text-center width-62_5">
                    <div class="center width-75">
                        <h2>
                            Looking at it now, last December. We were built to fall apart.
                            Then fall back together.
                        </h2>
                    </div>
                </div>
                <div class="column width-12_5"></div>
            </div>
            <div class="row">
                <div class="column width-37_5"></div>
                <div class="column width-50">
                    <p>
                        Morbi euismod magna ac lorem rutrum elementum. Donec viverra auctor
                        lobortis. Pellentesque eu est a nulla placerat dignissim. Morbi a enim in
                        magna semper bibendum. Etiam scelerisque, nunc ac egestas consequat, odio
                        nibh euismod nulla, eget auctor orci nibh vel nisi. Aliquam erat volutpat.
                        Mauris vel neque sit amet nunc gravida congue sed sit amet purus. Quisque
                        lacus quam, egestas ac tincidunt a, lacinia vel velit. Aenean facilisis
                        nulla vitae urna tincidunt.
                    </p>
                    <p>
                        Nam vestibulum, arcu sodales feugiat consectetur, nisl orci bibendum elit,
                        eu euismod magna sapien ut nibh. Donec semper quam scelerisque tortor.
                        Mauris vel neque sit amet nunc gravida congue.
                    </p>
                </div>
                <div class="column width-12_5"></div>
            </div>
        </div>
        <div class="fixed right">&nbsp;</div>
    </div>
</div>
</template>

<script>
export default {
  name: 'Layout',
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
    display: inline-block;
    margin: 0;
    padding: 0;
    text-align: left;
}
h1 {
    background-color: white;
    display: inline;
    font-size: 2em;
    padding: 0.2em;
}
h2 {
    font-size: 1.5em;
}
p {
    margin: 0;
    margin-bottom: 1em;
    padding: 0;
}
.absolute {
    position: absolute;
}
.background-image {
    background-image: url('../assets/Ji9qebSpSlSbnsWRZnDX__MG_9520.jpg');
    background-repeat: no-repeat;
    background-size: 100% auto;
    height: 0;
    margin-bottom: 3em;
    overflow: visible;
    padding-top: 66.67%;
    position: relative;
}
.bottom {
    bottom: 2em;
}
.center {
    margin: auto
}
.column {
    margin-right: -4px;
}
.content {
    left: 70px;
    height: 100%;
    width: calc(100% - 140px);
}
.fixed {
    height: 100%;
    width: 70px;
}
.left {
    float: left;
    left: 0;
}
.offset {
    top: 2.5em;
}
.relative {
    position: relative;
}
.right {
    float: right;
    right: 0;
}
.row {
    width: 100%;
}
.text-center {
    text-align: center;
}
.text-right {
    text-align: right;
}
.top {
    top: 1em;
}
.width-12_5 {
    width: 12.5%;
}
.width-25 {
    width: 25%;
}
.width-37_5 {
    width: 37.5%;
}
.width-50 {
    width: 50%;
}
.width-62_5 {
    width: 62.5%;
}
.width-75 {
    width: 75%
}
.width-85 {
    width: 85%
}
.width-100 {
    width: 100%;
}
</style>
