const staticCacheName = 'site-static';
const assets = [
	'/',
	'/static/css/style.css',
	'/static/css/responsive.css',
	'/static/css/bootstrap.min.css',
	'/static/css/main.min.css',
	'/static/js/bootstrap.min.js',
	'/static/js/main.min.js',
	'/static/js/script.js',
];
	
self.addEventListener('install', function(event){
    //console.log('[Service Worker], service worker installing', event);
	event.waitUntil(
	caches.open(staticCacheName).then(cache => {
		console.log('caching shell assets')
		cache.addAll(assets);
	})
	);
});

self.addEventListener('activate', function(event){
    console.log('[Service Worker], Activating service worker', event);
    return self.clients.claim();
});

self.addEventListener('fetch', function(event){
    //console.log('[Service Worker], Fetching service worker', event);
	event.respondWith(
		caches.match(event.request).then(cacheRes => {
			return cacheRes || fetch(event.request);
		})
	)
});