FROM python:3.11-slim

ARG USERNAME=fastapi
ARG USER_UID=1005
ARG USER_GID=1005

# Create non-root user and switch to the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
USER $USERNAME
# Add pip libraries default install path
ENV PATH="$PATH:/home/$USERNAME/.local/bin:/app"

COPY ./app /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]