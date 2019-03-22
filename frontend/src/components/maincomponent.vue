<template>
<div class="cont">  
<header>
  <nav class="main-nav">
    <ul>
      <li>
        <ul>
          <li><button v-on:click="set_url_router('Početna')" >POČETNA</button></li>
          <li><button v-on:click="set_url_router('Aktualno')" >AKTUALNO</button></li>
          <li><button v-on:click="set_url_router('Vijesti')" >VIJESTI</button></li>
          <li><button v-on:click="set_url_router('Sport')" >SPORT</button></li>
          <li><button v-on:click="set_url_router('Tech')" >TECH</button></li>
          <li><input type="text" name="search" v-model="query"></li>
          <li><button @click="getall()">Trazi</button></li>

        </ul>
      </li>
    </ul>
  </nav>
</header>
<section id="video" class="home">
  <h1>rssnews</h1>
  <h2>Kanali portala 24 sata</h2>
</section>
<section id="main-content">
  <div class="text-intro">
    <h2>{{url_router}}</h2>

  </div>

<div v-if="found">
  <div class="columns features" v-for="(data, index) in toshow" :key='index'>
    {{split_desc(data.description)}}
    <div class="one-half first">
      <img class="center" v-bind:src="image">
    </div>


    <div class="one-half second">
      <h3 >{{data.title}}</h3>
      <small class="text-muted"> Naziv kanala: {{ data.channel }} </small><br>
      <small class="text-muted"> Datum objave: {{format_date(data.date_posted)}}</small>
      <br>
      <br>
      <p>{{description}}</p>
      <br>
      <p><a v-bind:href="''+ data.link" class="more">Nastavi citati</a></p>
    </div>
  </div>
             
</div>


<div v-else>
  <div class="columns features" v-for="(data, index) in articles" :key='index'>
    {{split_desc(data.description)}}
    <div class="one-half first">
      <img class="center" v-bind:src="image">
    </div>


    <div class="one-half second">
      <h3 >{{data.title}}</h3>
      <small class="text-muted"> Naziv kanala: {{ data.channel }} </small><br>
      <small class="text-muted"> Datum objave: {{format_date(data.date_posted)}}</small>
      <br>
      <br>
      <p>{{description}}</p>
      <br>
      <p><a v-bind:href="''+ data.link" class="more">Nastavi citati</a></p>
    </div>
</div>
            
    
  </div>
          <div>Stranica: {{page}}</div>
          <button v-on:click="previouspage()" >Prethodna</button>
          <button v-on:click="nextpage()" >Slijedeca</button>


</section>
<footer>
  
  
  <div class="copyright"> | <a target="_blank" rel="nofollow" href="#">m</a> |</div>

</footer>


<div v-if="!pulled">{{ getArticles() }}</div>
<div v-once>{{ getCat() }}</div>

</div>
</template>



<script>

import axios from 'axios';


export default {
  
  name: 'maincomponent',
  data () {
    return {
      query: '',
      allarti: [],
      toshow: [],
      found: false,
      nextt: '1',

      
      url_router: 'Početna',

      cat: "http://127.0.0.1:8000/categories/",
      last: 'articles/?page=',
      pocetna: 'http://127.0.0.1:8000/articles/?page=',
      link: 'http://127.0.0.1:8000/articles/?page=',
      page: '1',
      prevpage: '1',
      cat_id:'',
      articles: [],
      categories: [],
      image: '',
      description: '',
      pulled: false,

      err: ''
    }
  }, 
  methods: {

    split_desc: function(desc){
      var splitted = desc.split(" />")
      var i = splitted[0]
      i = i.split('"')
      this.image = i[1]

      this.description = splitted[1]


    },

    format_date: function(fdate){
       
      var a = fdate.replace(/...Z$/, "h").replace("T", " ").split(" ")
      return a[0].split("-").reverse().join(".") + " u " + a[1]
    },

    set_url_router: function(setr){
      this.toshow = []
      this.found = false
      this.url_router = setr
      if (this.url_router == 'Početna'){
        this.link = this.pocetna
        this.getArticles()
        return
      }
      if (this.url_router == 'Aktualno'){
        this.cat_id = this.categories[0].id
        
      }
      if (this.url_router == 'Vijesti'){
        this.cat_id = this.categories[1].id
        
      }
      if (this.url_router == 'Sport'){
        this.cat_id = this.categories[2].id

      }
      if (this.url_router == 'Tech'){
        this.cat_id = this.categories[3].id
        
      }
      this.page ='1'
      this.link = this.cat + this.cat_id.toString() + "/" + this.last
      this.getArticles()
    },

    nextpage: function() {
      this.prevpage = this.page
      this.page = Number(this.page) + Number(1)

      this.page = this.page.toString()
      this.getArticles()

    },
    previouspage: function() {
      if (this.page > 1) {
        this.prevpage = this.page
        this.page = Number(this.page) - Number(1)
        this.page = this.page.toString()
        this.getArticles()
      }
      else {
        alert("Prva stranica")
      }

    },
    getCat: function(){
      this.pulled = true;

      axios.get(this.cat)
      .then((response)  =>  {
       
        this.categories = response.data.results;
      
      }, (error)  =>  {
        this.err = error;
      })
    },
   
    getArticles: function () {
      
      axios.get(this.link + this.page)
      .then((response)  =>  {
        this.pulled = true;

        if (this.url_router == 'Početna'){
          this.articles = response.data.results;
        }
        if (this.url_router != 'Početna'){
          this.articles = response.data;
        }
        this.pulled = true;
 
      }, (error)  =>  {
        this.pulled = true;
        this.page = this.prevpage;
        this.err = error;
      })
    },

    searchtd: function(){
        var i;
        var j;
      for (i=0; i<this.allarti.length ; i++){
        for (j=0; j<this.allarti[i].length; j++){
        
          var tit = this.allarti[i][j].title
          var desc = this.allarti[i][j].description

          if (tit.includes(this.query) || desc.includes(this.query)){
            
            this.toshow.push(this.allarti[i][j])
            this.found = true;
            
          }
          
        }

      }

    },

     getall: function(){

      this.nextt = Number(this.nextt) + 1
      this.nextt = this.nextt.toString()
      axios.get(this.pocetna + this.nextt)
      .then((response)  =>  {
       
        this.allarti.push(response.data.results)
        this.getall();
      
      }, (error)  =>  {
        this.searchtd()
        this.err = error;
      })
    },
    
    
  
  },
  

}

</script>


<style>


</style>