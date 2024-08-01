if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.app:app", port=80, host="127.0.0.1", reload=True)
