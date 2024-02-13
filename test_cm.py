from contextlib import asynccontextmanager

# Define an asynchronous context manager using @asynccontextmanager
@asynccontextmanager
async def my_async_context_manager():
    # Code to enter the context
    print("Entering the async context")
    
    try:
        # Yield control back to the caller
        yield "resource"  # This value can be accessed within the async with block
        
    finally:
        # Code to exit the context
        print("Exiting the async context")

# Using the asynchronous context manager
async def main():
    async with my_async_context_manager() as resource:
        print("Inside the async with block")
        print("Resource:", resource)

# Run the event loop
import asyncio
asyncio.run(main())