new Vue({
   el: '#starting',
   delimiters: ['${','}'],
   data: {
	   news: [],
	   search_term: '',
	   next: null,
	   previous: null,
 	},
 	mounted: function() {
 		this.getArticles();		 		
	},
	methods: {		
		getArticles: function() {
			let api_url = '/api/articles/';

			if (this.search_term !== '' && this.search_term !== null) {
				api_url += '?search='+this.search_term;
			}
			axios.get(api_url)
		      	.then((response) => {
		        	this.news = response.data.results;
		        	this.next = response.data.next;	
		        	this.previous = response.data.previous;
		      	})
		      	.catch((err) => {
		       	console.log(err);
		      	})
		    this.search_term = '';  
		},
		getCategory: function( category ) {
			axios.get('/api/articles/?category='+category)
		      	.then((response) => {
		        	this.news = response.data.results;
		        	this.next = response.data.next;	
		        	this.previous = response.data.previous;	
		      	})
		      	.catch((err) => {
		       	console.log(err);
		      	})
		},
		getNext: function() {
			axios.get(this.next)
		      	.then((response) => {
		        	this.news = response.data.results;
		        	this.next = response.data.next;	
		        	this.previous = response.data.previous;	
		      	})
		      	.catch((err) => {
		       	console.log(err);
		      	})
		},
		getPrevious: function() {
			axios.get(this.previous)
		      	.then((response) => {
		        	this.news = response.data.results;
		        	this.next = response.data.next;	
		        	this.previous = response.data.previous;	
		      	})
		      	.catch((err) => {
		       	console.log(err);
		      	})
		}
	}
});