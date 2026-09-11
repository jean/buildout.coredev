# Android/Termux stub: re-export the HTTP OTLP span exporter under the gRPC
# module path.  grpcio cannot be compiled on Android, so this shim lets
# plone.observability (which hardcodes the grpc import path) work at runtime
# via the HTTP transport instead.
#
# Point your collector at port 4318 (HTTP/protobuf) instead of 4317 (gRPC):
#   OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter,
)

__all__ = ["OTLPSpanExporter"]
