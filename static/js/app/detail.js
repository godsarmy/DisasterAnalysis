
(function () {
	var module = angular.module("detail-map", ["google-maps"]);
}());

function DetailController ($scope, $http) {
	
    $scope.markers = g_markers;

    $http.get('ajax-detail?latitude='+g_latitude+"&longitude="+g_longitude+"&timestamp="+g_timestamp).success(function(data) {
        $scope.early_events = data.early_events;
        $scope.late_events = data.late_events;
    });

    $scope.isCurrent = function(e) {
        return !(e._id == g_oid);
    };

	angular.extend($scope, {
		
		/** the initial center of the map */
		centerProperty: {
			latitude: g_latitude,
			longitude: g_longitude
		},
		
		/** the initial zoom level of the map */
		zoomProperty: 6,
		
		/** list of markers to put in the map */
		markersProperty: $scope.markers,
		
		// These 2 properties will be set when clicking on the map
		clickedLatitudeProperty: null,	
		clickedLongitudeProperty: null,
	});
}
