self.addEventListener('install', function(event){
    console.log('[Service Worker], service worker installing', event);
})

self.addEventListener('activate', function(event){
    console.log('[Service Worker], Activating service worker', event);
    return self.clients.claim();
})

self.addEventListener('fetch', function(event){
    console.log('[Service Worker], Fetching service worker', event);
})