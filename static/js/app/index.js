
(function () {
	var module = angular.module("index-map", ["google-maps"]);
}());

function IndexController ($scope) {
	
    $scope.markers = g_markers;

	angular.extend($scope, {
		
		/** the initial center of the map */
		centerProperty: {
			latitude: 36,
			longitude: 104
		},
		
		/** the initial zoom level of the map */
		zoomProperty: 4,
		
		/** list of markers to put in the map */
		markersProperty: $scope.markers,
		
		// These 2 properties will be set when clicking on the map
		clickedLatitudeProperty: null,	
		clickedLongitudeProperty: null,
	});
}
