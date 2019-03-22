new Vue({
   el: '#starting',
   delimiters: ['${','}'],
   data: {
	   news: [],
	   message: null,
	   search_term: '',
 	},
 	mounted: function() {
 		this.getItems();		 		
	},
	methods: {
		getItems: function() {
			let api_url = '/api/articles/';

			if (this.search_term !== '' && this.search_term !== null) {
				api_url += '?search='+this.search_term;
			}
			axios.get(api_url)
		      	.then((response) => {
		        	this.news = response.data.results;	
		      	})
		      	.catch((err) => {
		       	console.log(err);
		      	})
		}
	}
});