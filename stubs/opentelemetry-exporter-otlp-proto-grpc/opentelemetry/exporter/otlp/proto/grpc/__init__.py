# Android/Termux stub: grpcio cannot be compiled on Android.
# This package re-exports the HTTP OTLP exporter under the gRPC namespace so
# that code importing from opentelemetry.exporter.otlp.proto.grpc works at
# runtime.  Configure the OTLP endpoint with:
#
#   OTEL_EXPORTER_OTLP_ENDPOINT=http://<host>:4318   (HTTP port, not gRPC 4317)
#
# or set OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf explicitly.
