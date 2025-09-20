from django.shortcuts import render
from django.core.cache import cache
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


# Create your views here.


def get_cache_key(prefix, identifier=None):
    """Generate consistent cache keys"""
    if identifier:
        return f"{prefix}_{identifier}"
    return prefix


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request, *args, **kwargs):
        # Step 1: Create cache key
        cache_key = get_cache_key('user_list')
        
        # Step 2: Try to get from cache
        cached_data = cache.get(cache_key)
        
        if cached_data is not None:
            return Response(cached_data)
        
        # Step 3: Get fresh data
        response = super().list(request, *args, **kwargs)
        
        # Step 4: Store in cache
        cache.set(cache_key, response.data, timeout=300)  # 5 minutes cache
        
        return response
    
    def retrieve(self, request, *args, **kwargs):
        # Step 1: Create cache key with user ID
        user_id = kwargs.get('pk')
        cache_key = get_cache_key('user', user_id)
        
        # Step 2: Try to get from cache
        cached_data = cache.get(cache_key)
        
        if cached_data is not None:
            return Response(cached_data)
        
        # Step 3: Get fresh data
        response = super().retrieve(request, *args, **kwargs)
        
        # Step 4: Store in cache
        cache.set(cache_key, response.data, timeout=300)  # 5 minutes cache
        
        return response
    
    def create(self, request, *args, **kwargs):
        # Clear list cache when creating new user
        cache.delete(get_cache_key('user_list'))
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        # Clear both list cache and specific user cache
        user_id = kwargs.get('pk')
        cache.delete(get_cache_key('user_list'))
        cache.delete(get_cache_key('user', user_id))
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        # Clear both list cache and specific user cache
        user_id = kwargs.get('pk')
        cache.delete(get_cache_key('user_list'))
        cache.delete(get_cache_key('user', user_id))
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        # Clear both list cache and specific user cache
        user_id = kwargs.get('pk')
        cache.delete(get_cache_key('user_list'))
        cache.delete(get_cache_key('user', user_id))
        return super().destroy(request, *args, **kwargs)