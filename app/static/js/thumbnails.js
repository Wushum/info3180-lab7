app.factory('thumbnails', ['$http', function($http) {
  // Fetch JSON from server using HTTP GET request
  return $http.get('http://info3180lab7-wushum.c9users.io:8080/api/thumbnails') 
            .then(function(response) { 
              // Thumbnail data
              console.log(response.data);
              return response.data; 
            } 
            ,function(err) { 
              // Error info
              return err; 
            }); 
}]);
