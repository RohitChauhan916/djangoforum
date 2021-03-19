const staticCacheName = 'site-static';
const assets = [
	'/'
];
self.addEventListener('install', function(event){
    //console.log('[Service Worker], service worker installing', event);
	caches.open(staticCacheName).then(cache => {
		cache.addAll()
	})
});

self.addEventListener('activate', function(event){
    console.log('[Service Worker], Activating service worker', event);
    return self.clients.claim();
})

self.addEventListener('fetch', function(event){
    console.log('[Service Worker], Fetching service worker', event);
})