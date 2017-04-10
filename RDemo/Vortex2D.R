library(TDA)

# vortex
X<-circleUnif(n=1000, r=1)
V<-X[, c('x2', 'x1')]
colnames(V)<-c('v1', 'v2')
V[, 'v1']<-(-V[, 'v1'])
phaseSpace<-cbind(X, V)

gridDiag(X=phaseSpace)

# line checking
along.line<- function(point, x1, x2, tol=1e-6) {
  m21<- (x2-x1)/norm(x2-x1, type='2')
  mp1<- (point-x1)/norm(point-x1, type='2')
  m2p<- (x2-point)/norm(x2-point, type='2')
  Reduce(function(a, b) a & b, m21==mp1) & Reduce(function(a, b) a & b, m2p==m21)
}

# grid initialization
grid<- expand.grid(seq(-1, 1, 0.01), seq(-1, 1, 0.01))

# circle
X<- circleUnif(n=1000, r=1)
diag.info<- gridDiag(X=X, FUN=kde, h=0.3, lim=cbind(c(-1, 1), c(-1, 1)), by=0.01, sublevel = FALSE,
                     library = 'PHAT', printProgress=FALSE)

# circle and a line
X<- circleUnif(n=1000, r=1)
hl<- matrix(c(seq(-1, 1, 0.02), rep(0, 201)), ncol=2)
X<- rbind(X, hl)
diag.info<- gridDiag(X=X, FUN=kde, h=0.3, lim=cbind(c(-1, 1), c(-1, 1)), by=0.01, sublevel = FALSE,
                     library = 'PHAT', printProgress=FALSE)


# filled circle
in.circle<- mapply(function(x, y) {x*x+y*y<1}, grid[,1], grid[,2])
X<- grid[ in.circle,]
diag.info<- gridDiag(X=X, FUN=kde, h=0.3, lim=cbind(c(-1, 1), c(-1, 1)), by=0.01, sublevel = FALSE,
                     library = 'PHAT', printProgress=FALSE)

# filled hollow
in.hollow<- mapply(function(x, y) {x*x+y*y<1 & x*x+y*y>0.5}, grid[,1], grid[,2])
X<- grid[ in.hollow,]
diag.info<- gridDiag(X=X, FUN=kde, h=0.3, lim=cbind(c(-1, 1), c(-1, 1)), by=0.01, sublevel = FALSE,
                     library = 'PHAT', printProgress=FALSE)

# embedded circle
in.hollow<- mapply(function(x, y) {(x*x+y*y<1 & x*x+y*y>0.5) | (x*x+y*y<0.1)}, grid[,1], grid[,2])
X<- grid[ in.hollow,]
diag.info<- gridDiag(X=X, FUN=kde, h=0.3, lim=cbind(c(-1, 1), c(-1, 1)), by=0.01, sublevel = FALSE,
                     library = 'PHAT', printProgress=FALSE)

# along a line between two points
want<- mapply(function(x,y) {along.line(c(x,y), c(0,0), c(0,1)) | along.line(c(x,y), c(0,0), c(0.5,0.5)) | along.line(c(x,y), c(0.5,0.5), c(0,1))},
              grid[, 1], grid[, 2])
X<- grid[want,]
X<- X[ mapply(function(i) !is.na(X[i,1]) & !is.na(X[i,2]), 1:nrow(X)),]
diag.info<- gridDiag(X=X, FUN=kde, h=0.3, lim=cbind(c(-1, 1), c(-1, 1)), by=0.01, sublevel = FALSE,
                     library = 'Dionysus', printProgress=FALSE)

# two triangles
want<- mapply(function(x,y) {
  ctol<-1e-2
  along.line(c(x,y), c(0,0), c(0.3,0.3), ctol) | along.line(c(x,y), c(0,0), c(0.1,0.25), ctol) | along.line(c(x,y),c(0.1,0.25),c(0.3,0.3), ctol) | along.line(c(x,y),c(0.5,0.7),c(0.7,0.8), ctol)
}, grid[,1], grid[,2])
X<- grid[want,]
X<- X[ mapply(function(i) !is.na(X[i,1]) & !is.na(X[i,2]), 1:nrow(X)),]
diag.info<- gridDiag(X=X, FUN=kde, h=0.3, lim=cbind(c(-1, 1), c(-1, 1)), by=0.01, sublevel = FALSE,
                     library = 'Dionysus', printProgress=FALSE)

# surface sphere
grid3d<- expand.grid(seq(-1,1,0.05), seq(-1,1,0.05), seq(-1,1,0.05))
on.sphere<- mapply(function(x,y,z) x*x+y*y+z*z-0.15<1e-2, grid3d[, 1], grid3d[, 2], grid3d[, 3])
X<- grid3d[ on.sphere,]
diag.info<- gridDiag(X=X, FUN=kde, h=0.3, lim=cbind(c(-1, 1), c(-1, 1), c(-1, 1)), by=0.01, sublevel = FALSE,
                     library = 'Dionysus', printProgress=FALSE)

# torus
X<- torusUnif(10, a=1.8, c=5)
diag.info<- gridDiag(X=X, FUN=kde, h=0.3, lim=cbind(c(-1, 1), c(-1, 1), c(-1, 1)), by=0.01, sublevel = FALSE,
                     library = 'Dionysus', printProgress=FALSE)


# plotting
plot(X)
plot(diag.info$diagram)
plot(diag.info$diagram, barcode=TRUE)